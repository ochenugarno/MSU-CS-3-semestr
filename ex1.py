class Poly:
    def sigma(st, stepen):
        ans = str()
        if stepen == 0:
            return ''
        if stepen == 1:
            ans += '*' + st
            return ans
        else:
            ans += ('*' + st + '^' + str(stepen))
            return ans


    def check(self):
        for key, value in list(self.source.items()):
            if value == 0:
                self.source.pop(key)


    def __init__(self, lmao):
        self.source = lmao


    def __add__(self, other):
        if isinstance(other, int):
            other = Poly({(0, 0): other})
        result = Poly({})
        for self_key, self_value in self.source.items():
            result.source[self_key] = result.source.get(self_key, self_value)
        for other_key, other_value in other.source.items():
            result.source[other_key] = result.source.get(other_key, 0) + other_value
        result.check()
        return result


    def __sub__(self, other):
        if isinstance(other, int):
            other = Poly({(0, 0): other})
        result = Poly({})
        for self_key, self_value in self.source.items():
            result.source[self_key] = result.source.get(self_key, self_value)
        for other_key, other_value in other.source.items():
            result.source.get(other_key, 0)
            result.source[other_key] -= other_value
        result.check()
        return result


    def __mul__(self, other):
        if isinstance(other, int):
            other = Poly({(0, 0): other})
        res = Poly({})
        for self_key, self_value in self.source.items():
            p_el = Poly({})
            for other_key, other_value in other.source.items():
                p_el.source[(self_key[0] + other_key[0], self_key[1] + other_key[1])] = self_value * other_value
            res += p_el
        res.check()
        return res


    def __truediv__(self, denom):
        for value in self.source():
            value /= denom
        return self


    def __eq__(self, other):
        flag = True
        if len(self - other) != 0:
            flag = False
        return flag


    def __radd__(self, other):
        other = Poly({(0, 0): other})
        result = Poly({})
        for self_key, self_value in self.source.items():
            result.source[self_key] = result.source.get(self_key, self_value)
        result += other
        result.check()
        return result


    def __rsub__(self, other):
        other = {(0, 0): other}
        result = Poly()
        for self_key, self_value in self.source.items():
            result.source[self_key] = result.source.get(self_key, self_value)
        result -= other
        result.check()
        return result


    def __rmul__(self, other):
        other = Poly({(0, 0): other})
        res = Poly({})
        for self_key, self_value in self.source.items():
            p_el = Poly({})
            for other_key, other_value in other.source.items():
                p_el.source[(self_key[0] + other_key[0], self_key[1] + other_key[1])] = self_value * other_value
            res += p_el
        res.check()
        return res

    def __matmul__(self, other):
        return self * other


    def __repr__(self):
        ans = ''
        s = 0
        for key, value in self.source.items():
            if value > 0:
                if s > 0:
                    ans += (' + ' + str(value) + Poly.sigma('x', key[0]) + Poly.sigma('y', key[1]))
                    s += 1
                else:
                    ans += (str(value) + Poly.sigma('x', key[0]) + Poly.sigma('y', key[1]))
                    s += 1
            else:
                ans += (' - ' + str(-value) + Poly.sigma('x', key[0]) + Poly.sigma('y', key[1]))
                s += 1
        return ans


bruh1 = Poly({(2, 1): 1, (0, 0): 1})
bruh2 = Poly({(2, 1): -1, (0, 0): 1})
bruh1 *= bruh2
print(bruh1)