fn part_1() -> i32 {
    let (heading, depth) = include_str!("../../../inputs/2.txt")
        .lines()
        .map(|l| l.split_once(" ").unwrap())
        .fold((0, 0), |(heading, depth), (direction, value)| {
            match (direction, value.parse::<i32>().unwrap()) {
                ("forward", v) => (heading + v, depth),
                ("down", v) => (heading, depth + v),
                ("up", v) => (heading, depth - v),
                _ => unreachable!(),
            }
        });
    return heading * depth;
}

fn part_2() -> i32 {
    let (heading, depth, aim) = include_str!("../../../inputs/2.txt")
        .lines()
        .map(|l| l.split_once(" ").unwrap())
        .fold((0, 0, 0), |(heading, depth, aim), (direction, value)| {
            match (direction, value.parse::<i32>().unwrap()) {
                ("forward", v) => (heading + v, depth + aim * v, aim),
                ("down", v) => (heading, depth, aim + v),
                ("up", v) => (heading, depth, aim - v),
                _ => unreachable!(),
            }
        });
    return heading * depth;
}

fn main() {
    println!("part 1: {}", part_1());
    println!("part 2: {}", part_2());
}
