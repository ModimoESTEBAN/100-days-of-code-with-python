import probability_calc as pb

hat = pb.Hat(blue=4, red=2, green=6)

probab = pb.experiment(hat=hat,
                       expected_balls={"blue": 2,
                                       "red": 1},
                       num_balls_drawn=4,
                       num_experiments=3000)

print("Probability: ", probab)