import numpy as np
import matplotlib.pyplot as plt


def low_large_number_f():
    def fig_1():
        n = 45
        outcomes = np.random.randint(1,6+1, size=n)
        average_outcome = np.mean(outcomes)
        expected_value = round(np.random.uniform(3,4), 2)
        print(average_outcome)
        print(expected_value)
        plt.figure(figsize=(10, 30))
        plt.subplot(1, 3, 1)
        plt.plot(list(range(0,n)), outcomes, 'ro')

    # number_of_trials  = 500
    # pieces_outcomes = np.random.randint(0,1+1, size=number_of_trials )
    # pieces_average_outcome = np.mean(pieces_outcomes)
    # success = int(pieces_average_outcome * 100)
    # failure = 100 - success
    # print(pieces_outcomes)
    # print(pieces_average_outcome)
    # print(f"success rate {success}%")
    # print(f"failure rate {failure}%")

    def fig_2():
        number_of_trials = 500  # play this this number
        p = 0.5  # expected value of the coin
        #############################################
        #     playing with the number of trials     #
        #############################################
        trials = np.arange(1, number_of_trials + 1, 1)
        results = [np.mean(np.random.randint(0, 1 + 1, n)) for n in trials]

        #############################################
        #            plotting the results           #
        #############################################

        plt.subplot(1, 3, 2)

        plt.plot(results, label='empirical means')
        plt.plot([p] * len(results), label='p', color="red")

        plt.title('Law of Large Numbers : The empirical mean converges towards the theoretical mean')
        plt.xlabel('Number of trials')
        plt.ylabel('Theoretical mean')

        plt.legend(loc='best')


    def fig_3():

        #############################################
        #     playing with the number of trials     #
        #############################################
        p = 0.7
        n = 10
        N = 1000

        trials = np.arange(1, N + 1, 1)
        results = [np.mean(np.random.binomial(n=n, p=p, size=N)) for N in trials]

        #############################################
        #            plotting the results           #
        #############################################

        expected_value_coins = None
        plt.subplot(1, 3, 3)

        plt.plot(results, label='empirical means')
        plt.plot([expected_value_coins] * len(results), label='mu', color="red")
        plt.xlabel('Number of trials')
        plt.ylabel('Theoretical mean')

        plt.legend(loc='best')

    fig_1()
    fig_2()
    fig_3()

    plt.show()