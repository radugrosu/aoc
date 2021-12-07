#![feature(drain_filter)]

fn part_1(input: &str) -> u32 {
    let num_bits = input.lines().next().unwrap().len();
    let num_lines = input.lines().count();
    let gamma = input
        .lines()
        .map(|line| usize::from_str_radix(line, 2).unwrap())
        .fold(vec![0; num_bits], |count, int| {
            count
                .into_iter()
                .enumerate()
                .map(|(i, n)| n + ((int & (1 << i)) >> i))
                .collect()
        })
        .into_iter()
        .enumerate()
        .map(|(i, n)| ((n >= num_lines / 2) as u32) << i)
        .sum::<u32>();
    let epsilon = !gamma & ((1 << num_bits) - 1);
    gamma * epsilon
}

fn part_2(input: &str) -> usize {
    let num_bits = input.lines().next().unwrap().len();
    let numbers = input
        .lines()
        .map(|line| usize::from_str_radix(line, 2).unwrap())
        .collect::<Vec<_>>();

    let oxygen = (0..num_bits)
        .rev()
        .scan(numbers.clone(), |oxy, i| {
            let one = oxy.iter().filter(|n| (*n & 1 << i) > 0).count() >= (oxy.len() + 1) / 2;
            oxy.drain_filter(|n| (*n & 1 << i > 0) != one);
            oxy.first().copied()
        })
        .last()
        .unwrap();

    let co2 = (0..num_bits)
        .rev()
        .scan(numbers.clone(), |c, i| {
            let one = c.iter().filter(|n| (*n & 1 << i) > 0).count() >= (c.len() + 1) / 2 as usize;
            c.drain_filter(|n| (*n & 1 << i > 0) == one);
            c.first().copied()
        })
        .last()
        .unwrap();
    oxygen * co2
}

fn main() {
    let input = include_str!("../../../inputs/3.txt");
    let test_input: &str =
        "00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010\n";
    assert_eq!(part_1(test_input), 198);
    println!("part 1: {}", part_1(input));

    assert_eq!(part_2(test_input), 230);
    println!("part 2: {}", part_2(input));
}
