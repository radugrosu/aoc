use std::collections::{HashMap, VecDeque};

fn score_corrupted_line(line: &str) -> Option<char> {
    let mut stack = VecDeque::new();
    let open = HashMap::from([('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')]);
    for c in line.chars() {
        if open.contains_key(&c) {
            stack.push_back(c);
        } else {
            match stack.pop_back() {
                Some(v) => match open[&v] == c {
                    true => continue,
                    false => return Some(c),
                },
                None => return Some(c),
            }
        }
    }
    None
}

fn part_1(input: &str) -> i32 {
    let score_map = HashMap::from([(')', 3), (']', 57), ('}', 1197), ('>', 25137)]);
    let mut score = 0;
    for line in input.lines() {
        match score_corrupted_line(line) {
            Some(c) => score += score_map[&c],
            None => continue,
        }
    }
    score
}

fn complete_line(line: &str) -> Option<String> {
    let mut stack = VecDeque::new();
    let open = HashMap::from([('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')]);
    for c in line.chars() {
        if open.contains_key(&c) {
            stack.push_back(c);
        } else {
            match stack.pop_back() {
                Some(v) => match open[&v] == c {
                    true => continue,
                    false => return None,
                },
                None => break,
            }
        }
    }
    Some(stack.iter().map(|c| open[c]).rev().collect::<String>())
}

fn score_completed_line(chars: &String) -> u64 {
    let score_map = HashMap::from([(')', 1), (']', 2), ('}', 3), ('>', 4)]);
    let mut score = 0;
    for c in chars.chars() {
        score = 5 * score + score_map[&c]
    }
    return score;
}

fn part_2(input: &str) -> u64 {
    let mut scores = Vec::new();
    for line in input.lines() {
        match complete_line(line) {
            Some(s) => scores.push(score_completed_line(&s)),
            None => continue,
        }
    }
    scores.sort();
    scores[scores.len() / 2]
}

fn main() {
    let test_input = include_str!("../../../inputs/10_test.txt").trim();
    let real_input = include_str!("../../../inputs/10.txt").trim();
    assert_eq!(part_1(test_input), 26397);
    println!("part 1: {}", part_1(real_input));

    assert_eq!(part_2(test_input), 288957);
    println!("part 2: {}", part_2(real_input));
}
