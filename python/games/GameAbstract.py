from abc import abstractmethod


class GameAbstract:
    #   Creates and executes query for a gamemode to get player points
    #   Runs a game's method corresponding to how we what to calculate scores (auto, new, num)
    #
    #   Args:
    #       cur - cursor to run query
    #       player - player whose scores we are trying to retrieve
    #       mccnum - how we what to calculate scores
    #       query - template of query to run
    #   Return:
    #       Nothing, runs method in gamemode class
    @abstractmethod
    def calc(self, cur, player: str, mccnum: str, query) -> int:
        player = '"' + player + '"'
        query = query.replace("player", player)
        cur.execute(query)
        data = cur.fetchall()

        if mccnum == "auto":
            return self.calcAuto(data)
        elif mccnum == "new":
            return self.calcNew(data)
        else:
            return self.calcByOne(data, mccnum)

    # Select the string that is showing a range which the num is between
    # Args:
    #   num - number to find in the ranges
    #   keys - all ranges applicable to a game's scoring
    # Return:
    #   string indicating which range the number falls under
    @abstractmethod
    def getKeyFromNum(self, num: int, keys):
        for key in keys:
            try:
                keyNums = key.split("-")
                if int(keyNums[0]) <= int(num) <= int(keyNums[1]):
                    return key
            except Exception:
                if int(key) == int(num):
                    return key
        return ArithmeticError(num + " " + str(keys))
