use std::collections::HashMap;

fn read_input(input: &str) -> (&str, HashMap<&str, &str>) {
    let (elements, rules) = input.split_once("\n\n").unwrap();
    (
        elements,
        rules
            .lines()
            .map(|l| l.split_once(" -> ").unwrap())
            .collect::<HashMap<_, _>>(),
    )
}

fn react(counts: &HashMap<String, u64>, rules: &HashMap<&str, &str>) -> HashMap<String, u64> {
    let mut new_counts = HashMap::<String, u64>::new();
    for (pair, &count) in counts {
        let produced = rules[&pair[..]];
        let key = [&pair[..1], produced].join("");
        *new_counts.entry(key).or_insert(0) += count;
        let key = [produced, &pair[1..]].join("");
        *new_counts.entry(key).or_insert(0) += count;
    }
    new_counts
}

fn grow(elements: &str, rules: HashMap<&str, &str>, steps: u32) -> u64 {
    let mut counts = HashMap::<String, u64>::new();
    for i in 0..elements.len() - 1 {
        let key = elements[i..i + 2].to_string();
        *counts.entry(key).or_insert(0) += 1;
    }
    for _ in 0..steps {
        counts = react(&counts, &rules);
    }
    let mut element_counts = HashMap::new();
    for (key, count) in counts {
        *element_counts.entry(key[..1].to_string()).or_insert(0) += count;
    }
    let last = elements[elements.len() - 1..].to_string();
    *element_counts.entry(last).or_insert(0) += 1;
    let min = element_counts.values().min().unwrap();
    let max = element_counts.values().max().unwrap();
    max - min
}

fn part_1(input: &str) -> u64 {
    let (elements, rules) = read_input(input);
    grow(elements, rules, 10)
}

fn part_2(input: &str) -> u64 {
    let (elements, rules) = read_input(input);
    grow(elements, rules, 40)
}
fn main() {
    let test_input = include_str!("../../../inputs/14_test.txt").trim();
    let real_input = include_str!("../../../inputs/14.txt").trim();
    assert_eq!(part_1(test_input), 1588);
    println!("part 1: {}", part_1(real_input));
    assert_eq!(part_2(test_input), 2188189693529);
    println!("part 2:\n{}", part_2(real_input));
}
