fn part_1() -> u16 {
    let mut num_larger: u16 = 0;
    let mut current: u16;
    let mut previous: u16;
    let inputs = include_str!("../../../inputs/1.txt")
        .lines()
        .map(|n| n.parse().unwrap())
        .collect::<Vec<u16>>();
    for i in 1..inputs.len() {
        current = *inputs.get(i).unwrap();
        previous = *inputs.get(i - 1).unwrap();
        if current > previous {
            num_larger += 1;
        }
    }
    num_larger
}

fn part_2() -> u16 {
    let mut num_larger: u16 = 0;
    let mut current: u16;
    let mut previous: u16;
    let inputs = include_str!("../../../inputs/1.txt")
        .lines()
        .map(|n| n.parse().unwrap())
        .collect::<Vec<u16>>();
    for i in 3..inputs.len() {
        current = inputs[i - 2..=i].iter().sum();
        previous = inputs[i - 3..i].iter().sum();
        if current > previous {
            num_larger += 1;
        }
    }
    num_larger
}

fn main() {
    println!("part 1: {}", part_1());
    println!("part 2: {}", part_2());
}
