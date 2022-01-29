# Done by Teodor Ciobanu, Los Angeles, Jan 26, 2022

inp = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1]
seat_n = 2
# given inp list is the availability seats where 1 is blocked and 0 is available
# the naming of the seat can be easily processed with the indexing system
# given seat_n the number of the seats required to be reserved


aval_seat_ind = [x for x in range(len(inp)) if inp[x] == 0]

if len(aval_seat_ind) < seat_n:
    print("Not enough available seats")

else:
    dist_list = []
    for i in range(len(aval_seat_ind)-seat_n+1):
        dist_list.append(aval_seat_ind[i + seat_n-1] - aval_seat_ind[i] + 1)
    min_dist = min(dist_list)
    min_ind = dist_list.index(min_dist)
    res = aval_seat_ind[min_ind:min_ind + seat_n]
    print("The closest to each other seats are indexes {0} (where the firts seat index is 0)".format(res))
    # indexes can easily be converted to the seat naming if it's the case
        




