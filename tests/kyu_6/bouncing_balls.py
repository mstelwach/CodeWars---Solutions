def bouncingBall(h, bounce, window):
    if bounce < 1 and bounce > 0 and window < h and h > 0:
        total = 0
        while(h >= window):
            total += 2
            h *= bounce
        return total - 1
    else:
        return -1

