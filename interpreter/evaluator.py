from typing import Any


class Environment:
    def __init__(self, parent: "Environment | None" = None):
        self.vars: dict[str, Any] = {}
        self.parent = parent

    def get(self, name: str) -> Any:
        if name in self.vars:
            return self.vars[name]
        if self.parent is not None:
            return self.parent.get(name)
        raise NameError(f"Nieznana zmienna: {name}")

    def set(self, name: str, value: Any) -> None:
        self.vars[name] = value

    def child(self) -> "Environment":
        return Environment(parent=self)


class ExpressionEvaluator:
    def __init__(self, state, env: Environment):
        self.state = state
        self.env = env

    # -- Dispatch
    def eval(self, ctx) -> Any:
        cls_name = type(ctx).__name__
        method = getattr(self, f"eval_{cls_name}", None)
        if method is None:
            # Fallback - np. jeśli to 'ConditionContext' z jednym dzieckiem expression
            if hasattr(ctx, "expression") and callable(ctx.expression):
                inner = ctx.expression()
                if inner is not None and not isinstance(inner, list):
                    return self.eval(inner)
            raise RuntimeError(f"Nieobsługiwany węzeł wyrażenia: {cls_name}")
        return method(ctx)

    # -- Literały / zmienne
    def eval_ExprNumContext(self, ctx):
        return float(ctx.NUMBER().getText())

    def eval_ExprStrContext(self, ctx):
        return ctx.STRING().getText().strip('"')

    def eval_ExprVarContext(self, ctx):
        return self.env.get(ctx.IDENTIFIER().getText())

    def eval_ExprParenContext(self, ctx):
        return self.eval(ctx.expression())

    # -- Arytmetyka
    def eval_ExprAddSubContext(self, ctx):
        a = self.eval(ctx.expression(0))
        b = self.eval(ctx.expression(1))
        return a + b if ctx.op.text == "+" else a - b

    def eval_ExprMulDivContext(self, ctx):
        a = self.eval(ctx.expression(0))
        b = self.eval(ctx.expression(1))
        if ctx.op.text == "*":
            return a * b
        if b == 0:
            raise ZeroDivisionError("Dzielenie przez zero w wyrażeniu")
        return a / b

    # -- Porównania i logika
    def eval_ExprCompareContext(self, ctx):
        a = self.eval(ctx.expression(0))
        b = self.eval(ctx.expression(1))
        op = ctx.op.text
        if op in (">",):   return a > b
        if op in ("<",):   return a < b
        if op in (">=",):  return a >= b
        if op in ("<=",):  return a <= b
        if op in ("==", "="): return a == b
        raise RuntimeError(f"Nieznany operator porównania: {op}")

    def eval_ExprLogicContext(self, ctx):
        op = ctx.op.text
        a = self.eval(ctx.expression(0))
        # short-circuit
        if op in ("oraz", "&&"):
            return bool(a) and bool(self.eval(ctx.expression(1)))
        return bool(a) or bool(self.eval(ctx.expression(1)))

    def eval_ExprNotContext(self, ctx):
        return not bool(self.eval(ctx.expression()))

    # -- Dostęp do stanu
    def eval_ExprStateContext(self, ctx):
        return self.eval(ctx.stateRef())

    def eval_StateSpeedContext(self, ctx):
        return float(self.state.speed)

    def eval_StateHeadingContext(self, ctx):
        return float(self.state.heading)

    def eval_StateWindFieldContext(self, ctx):
        field = ctx.windField().getText().lower()
        wind = self.state.wind
        mapping = {
            "sila":      wind.beaufort,
            "siła":      wind.beaufort,
            "beaufort":  wind.beaufort,
            "kierunek":  wind.direction,
            "kier":      wind.direction,
            "predkosc":  wind.speed,
            "prędkość":  wind.speed,
            "kn":        wind.speed,
            "wezly":     wind.speed,
            "węzły":     wind.speed,
        }
        if field not in mapping:
            raise RuntimeError(
                f"Nieznane pole wiatru: '{field}'. "
                f"Dostępne: sila, kierunek, predkosc"
            )
        return float(mapping[field])

    def eval_StateSailFieldContext(self, ctx):
        sail_name = ctx.sail().getText()
        field = ctx.IDENTIFIER().getText().lower()
        key = self.state.normalize_sail_key(sail_name)
        sail = self.state.sails.get(key)
        if sail is None:
            raise RuntimeError(f"Nieznany żagiel: {sail_name}")
        mapping = {
            "stan":    sail.state.value,
            "kat":     sail.angle,
            "kąt":     sail.angle,
            "ref":     sail.reef_percent,
            "refy":    sail.reef_percent,
            "szot":    sail.sheet_tension,
            "szoty":   sail.sheet_tension,
        }
        if field not in mapping:
            raise RuntimeError(
                f"Nieznane pole żagla: '{field}'. "
                f"Dostępne: stan, kat, ref, szot"
            )
        return mapping[field]