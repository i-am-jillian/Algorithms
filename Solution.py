from Marriage import Marriage
from itertools import permutations


class Solution:

    def __init__(self, number, women, men):
        """
        The constructor exists only to initialize variables. You do not need to change it.
        :param number: The number of members
        :param men: The preference list of men, as a dictionary.
        :param women: The preference list of the women, as a dictionary.
        """
        self.num = number
        self.men = men
        self.women = women
        self.count = 0
        self.stable_matchings = []

    def output_stable_matchings(self):
        """
        This method both computes and returns the stable matchings
        :return: the list of stable matchings
        """

        #making all possible permutations of men and assigning them to a woman
        #for every member men 1 to n, we assign each man to a woman
        for allMen in permutations(range(1, self.num +1)): 
            #empty dict to store one complete matching
            matching = {}
            #assign each woman to the man at pposition i in the permutation
            for i in range(self.num):
                matching[i+1] = allMen[i]
                #we reverse the matching from dictionary to get an object of lists to append to marriage
                #instead of k,v we have man, woman
            manToWoman = {v: k for k, v in matching.items()}

            #after having matchings, we gonna confirm they are stable
            #we assign a boolean to check if the match is stable or not, so we start assumming it is
            is_stable = True
            #iterrating throguh every woman to check if theres a blocking pair
            for w in self.women:
                #looking what current man is matched with woman w
                currentMan = matching[w]
                #iterating through every other man to check if they prefer w over their current match
                for m in range(1, self.num + 1):
                    if m == currentMan:
                        continue
                    #if w prefers m over current man, and m prefers w over its current woman, return false
                    if self.women[w].index(m) < self.women[w].index(currentMan) and self.men[m].index(w) < self.men[m].index(manToWoman[m]):
                        is_stable = False
                        break
                #if unstabe pair found, stop checking for this matching
                if not is_stable:
                    break
            #if matching is stable, we create a list of Marriage objects and append the matching to the list
            if is_stable:
                marriage_list = [Marriage(matching[w], w) for w in sorted(matching)]
                self.stable_matchings.append(marriage_list)

            #check if the matching is stable
        return self.stable_matchings
