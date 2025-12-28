from train import train_sarsa
def main():
    training = train_sarsa(5000, 5, 5, 4)
    print(training.q_values)
    return training.q_values



if __name__ == "__main__":
    main()
