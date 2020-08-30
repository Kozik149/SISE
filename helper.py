
class Helper:
    def track(self, v):
        data = []
        current_v = v
        data.append(current_v)
        while (current_v.parent is not None):
            current_v = current_v.parent
            data.append(current_v)
        return data