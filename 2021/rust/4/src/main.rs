use std::collections::BTreeMap;

const ROW: u32 = 0b11111;
const COL: u32 = 0b100001000010000100001;

pub fn part_1(input: &str) -> u32 {
    let (nums, boards) = input.split_once("\n\n").unwrap();

    let mut boards: Vec<(BTreeMap<u8, usize>, u32)> = boards
        .split("\n\n")
        .map(|b| {
            (
                b.split_whitespace()
                    .enumerate()
                    .map(|(i, n)| (n.parse().unwrap(), i))
                    .collect(),
                0,
            )
        })
        .collect();

    let (board, mark, num) = nums
        .split(',')
        .map(|n| n.parse().unwrap())
        .find_map(|n| {
            boards.iter_mut().find_map(|(b, m)| {
                b.get(&n)
                    .map(|i| *m |= 1 << *i)
                    .filter(|_| (0..5).any(|i| *m >> i & COL == COL || *m >> (i * 5) & ROW == ROW))
                    .map(|_| (b.clone(), *m, n))
            })
        })
        .unwrap();

    board
        .into_iter()
        .map(|(n, i)| (mark >> i & 1 ^ 1) * n as u32 * num as u32)
        .sum::<u32>()
}

fn main() {
    let real_input = include_str!("../../../inputs/4.txt");
    let test_input = include_str!("../../../inputs/4_test.txt");
    assert_eq!(part_1(test_input), 4512);
    println!("part 1: {}", part_1(real_input));

    // assert_eq!(part_2(test_input), 230);
    // println!("part 2: {}", part_2(input));
}
