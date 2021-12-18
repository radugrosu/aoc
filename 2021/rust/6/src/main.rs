use std::collections::HashMap;

fn part_1(input: &str, days: u16) -> u64 {
    let fish = input
        .split(",")
        .map(|i| i.parse().unwrap())
        .collect::<Vec<u8>>();
    let mut cache = HashMap::<(u8, u16), u64>::new();
    for i in 0..=8 {
        cache.insert((i, 0), 1);
    }
    for d in 1..=days {
        for a in 0..=8 {
            if a == 0 {
                cache.insert(
                    (0, d),
                    *cache.get(&(6, d - 1)).unwrap() + *cache.get(&(8, d - 1)).unwrap(),
                );
            } else {
                cache.insert((a, d), *cache.get(&(a - 1, d - 1)).unwrap());
            }
        }
    }
    fish.into_iter()
        .fold(0, |s, f| s + *cache.get(&(f, days)).unwrap())
}

fn main() {
    let test_input = include_str!("../../../inputs/6_test.txt").trim();
    let real_input = include_str!("../../../inputs/6.txt").trim();
    assert_eq!(part_1(test_input, 18), 26);
    println!("part 1: {}", part_1(real_input, 80));
    println!("part 2: {}", part_1(real_input, 256));
}
