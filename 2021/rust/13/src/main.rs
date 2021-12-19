use std::collections::HashSet;
// use std::time::Instant;

fn process_input(input: &str) -> (HashSet<(u32, u32)>, Vec<(char, u32)>) {
    let (dots, instructions) = input.split_once("\n\n").unwrap();
    let dots = dots
        .lines()
        .map(|l| {
            let (a, b) = l.split_once(",").unwrap();
            (a.parse().unwrap(), b.parse().unwrap())
        })
        .collect::<HashSet<_>>();
    let instructions = instructions
        .lines()
        .map(|l| {
            let (a, b) = l.split_once("=").unwrap();
            (a.to_string().chars().last().unwrap(), b.parse().unwrap())
        })
        .collect::<Vec<_>>();
    (dots, instructions)
}

fn fold(dots: HashSet<(u32, u32)>, instruction: (char, u32)) -> HashSet<(u32, u32)> {
    let (kind, anchor) = instruction;
    let mut to_add = HashSet::<(u32, u32)>::new();
    let mut to_remove = HashSet::<(u32, u32)>::new();
    for (x, y) in dots.iter() {
        if kind == 'x' && x > &anchor {
            to_add.insert((2 * anchor - *x, *y));
            to_remove.insert((*x, *y));
        }
        if kind == 'y' && y > &anchor {
            to_add.insert((*x, 2 * anchor - *y));
            to_remove.insert((*x, *y));
        }
    }

    dots.union(&to_add)
        .cloned()
        .collect::<HashSet<(u32, u32)>>()
        .difference(&to_remove)
        .cloned()
        .collect()
}

fn repr(dots: &HashSet<(u32, u32)>) -> String {
    let mut m = 0;
    let mut n = 0;
    for (x, y) in dots.iter() {
        if x > &m {
            m = *x;
        }
        if y > &n {
            n = *y;
        }
    }
    let mut table = Vec::<Vec<&str>>::new();
    for i in 0..n + 1 {
        let mut row = Vec::<&str>::new();
        for j in 0..m + 1 {
            if dots.contains(&(j, i)) {
                row.push(&"#");
            } else {
                row.push(&".");
            }
        }
        table.push(row);
    }
    table
        .iter()
        .map(|v| v.join(""))
        .collect::<Vec<_>>()
        .join("\n")
}

fn part_1(inputs: &str) -> usize {
    let (dots, instructions) = process_input(inputs);
    fold(dots, instructions[0]).len()
}
fn part_2(inputs: &str) -> String {
    let (mut dots, instructions) = process_input(inputs);
    for instruction in instructions.iter() {
        dots = fold(dots, *instruction)
    }
    repr(&dots)
}

fn main() {
    let test_input = include_str!("../../../inputs/13_test.txt").trim();
    let real_input = include_str!("../../../inputs/13.txt").trim();
    assert_eq!(part_1(test_input), 17);
    println!("part 1: {}", part_1(real_input));
    println!("part 2:\n{}", part_2(real_input));
}
