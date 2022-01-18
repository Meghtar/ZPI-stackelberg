# TODO: add array/map containing Pi_idle/Pi_busy/Pi_open/Pi_close and c's values
# if they are needed of course

# gain_and_costs = [{
#     "number": 1,
#     "gain": 1,
#     "attack_costs": [1, 1, 1]
# },
# {
#     "number": 2,
#     "gain": 1,
#     "attack_costs": [1, 2, 3]
# }]

attack_probabilities = {
    "countermeasure_1": [0, 0.1, 1, 0.9],
    "countermeasure_2": [0, 0.1, 1, 0.9],
    "countermeasure_3": [0, 0.1, 1, 0.9]
}

# śr. zaradczy/atak | sqli | phising | MiTM | DDoS | reverse
# backup            |`0.1  |1        | 1    | 1    | 0.2
# MFA               |1     |0        | 0.1  | 1    | 0.5
# anty-DDoS         |0.2   |0.5      | 0.5  | 0.1  | 1
# Centralizacja API |0.5   |1        | 0.4  | 1    | 0.4
# Hardening         |0.1   |0.5      | 0.5  | 1    | 0.2

attack_and_remedy_prob = [
    [0.1, 1, 1, 1, 0.2],
    [1, 0, 0.1, 1, 0.5],
    [0.5, 1, 0.4, 1, 0.4],
    [0.2, 0.5, 0.5, 0.1, 1],
    [0.1, 0.5, 0.2, 1, 0.2]
]

# attack_probabilities = {
#     "countermeasure_1" : [0, 0.1, 1, 0.9],
#     "countermeasure_2" : [0, 0.1, 1, 0.9],
#     "countermeasure_3" : [0, 0.1, 1, 0.9]
# }

# tab 6
# sqli | phish | mitm | ddos | rev
# backup
# mfa
# centr api
# anty-ddos
# hardening ?
attack_probabilities = [
    [0.2, 0.7, 0.5, 1, 0.95],
    [0.6, 0.1, 0.1, 1, 0.7],
    [0.25, 0.95, 0.5, 1, 0.15],
    [0.5, 0.95, 0.9, 0.05, 1],
    [0.15, 0.75, 0.5, 0.7, 0.1]
]

# tab 5 - to be follower gains and costs?
# attacker gain | a1cost | a2cost | a3cost | a4cost | a5cost
# asset nr vvv
backup_gains_and_costs_follower = [
    [40, 20, 20, 50, 10, 70],
    [40, 20, 20, 40, 10, 20],
    [80, 30, 20, 70, 10, 30],
    [100, 60, 20, 80, 15, 50],
    [20, 40, 10, 60, 10, 50]
]
# adjusted, gain must always be bigger than costs (???)
gains_and_costs_follower = [
    [40, 4, 4, 20, 2, 39],
    [40, 4, 4, 39, 2, 10],
    [80, 35, 20, 50, 1, 17],
    [100, 45, 20, 70, 15, 25],
    [20, 40, 10, 10, 7, 18]
]

# tab 5a - to be leader gains and costs?, currently it's just costs
# working asset gain | backups | MFA | API centralization? | anty-DDOS | hardening/pentests
# asset nr vvv
gain_and_costs_leader = [
    [40, 50, 30, 20, 5, 10],
    [50, 20, 30, 5, 10, 20],
    [40, 20, 35, 25, 15, 15],
    [80, 60, 35, 30, 25, 5],
    [40, 10, 20, 10, 10, 30]
]
