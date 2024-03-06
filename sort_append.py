if __name__ == '__main__':
    data, scores = [], []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name,score])
        scores.append(score)
    x = sorted(set(scores))[1]
    for name , score in sorted(data):
        if score == x:
            print(name)