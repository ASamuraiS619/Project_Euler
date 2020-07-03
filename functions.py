def primes_up_to(number):
    if number < 2:
        prime_numbers = None
    elif number <= 4 :
        prime_numbers = [2]
    else:
        # 検査の上限値
        border_line = int(number ** 0.5)
        prime_numbers = [2]
        target_list = list(range(3, number + 1, 2))

        while True:
            mesh_number = min(target_list)
            # 検査がborder_lineを超えると残りは全て素数なのでprime_numbersへ。
            if mesh_number > border_line:
                prime_numbers.extend(target_list)
                break
            prime_numbers.append(mesh_number)

            # mesh_numberで篩いにかける。割り切れなかったものを次の候補へ
            tmp_target_list = []
            for i in target_list:
                if i % mesh_number != 0:
                    tmp_target_list.append(i)
            target_list = tmp_target_list

        return prime_numbers
