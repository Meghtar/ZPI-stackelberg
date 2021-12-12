# TODO: add array/map containing Pi_idle/Pi_busy/Pi_open/Pi_close and c's values

gain_and_costs = [{
    "number": 1,
    "gain": 1,
    "attack_costs": [1, 1, 1]
},
{
    "number": 2,
    "gain": 1,
    "attack_costs": [1, 2, 3]
}]

attack_probabilities = {
    "countermeasure_1" : [0, 0.1, 1, 0.9],
    "countermeasure_2" : [0, 0.1, 1, 0.9],
    "countermeasure_3" : [0, 0.1, 1, 0.9]
}

# śr. zaradczy/atak | sqli | phising | MiTM | DDoS | reverse
# backup            |`0.1  |1        | 1    | 1    | 0.2
# MFA               |1     |0        | 0.1  | 1    | 0.5
# Centralizacja API |0.5   |1        | 0.4  | 1    | 0.4
# anty-DDoS         |0.2   |0.5      | 0.5  | 0.1  | 1
# Hardening         |0.1   |0.5      | 0.5  | 1    | 0.2

attack_and_remedy_prob = [
    [0.1, 1  , 1  , 1  , 0.2],
    [1  , 0  , 0.1, 1  , 0.5],
    [0.5, 1  , 0.4, 1  , 0.4],
    [0.2, 0.5, 0.5, 0.1, 1  ],
    [0.1, 0.5, 0.2, 1  , 0.2]
]

