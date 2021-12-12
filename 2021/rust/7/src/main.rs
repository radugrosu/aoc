fn part_1(input: &str) -> i32 {
    let mut numbers = input
        .split(",")
        .map(|i| i.parse().unwrap())
        .collect::<Vec<i32>>();

    numbers.sort();
    let median = numbers[numbers.len() / 2];
    numbers.iter().fold(0, |a, i| a + (i - median).abs())
}

fn part_2(input: &str) -> i32 {
    let numbers = input
        .split(",")
        .map(|i| i.parse().unwrap())
        .collect::<Vec<i32>>();

    println!("{}",     (numbers.iter().sum::<i32>() / numbers.len() as i32));
    
    (numbers.iter().sum::<i32>() / numbers.len() as i32..)
        .take(2)
        .map(|t| {
            numbers
                .iter()
                .map(|n| {
                    let d = (n - t).abs();
                    d * (d + 1) / 2
                })
                .sum::<i32>()
        })
        .min()
        .unwrap()
}

fn main() {
    let test_input = include_str!("../../../inputs/7_test.txt").trim();
    let real_input = include_str!("../../../inputs/7.txt").trim();
    assert_eq!(part_1(test_input), 37);
    println!("part 1: {}", part_1(real_input));

    assert_eq!(part_2(test_input), 168);
    println!("part 2: {}", part_2(real_input));
}
