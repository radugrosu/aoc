use std::collections::{HashMap, HashSet};
use std::time::Instant;

fn build_graph(input: &str) -> HashMap<&str, HashSet<&str>> {
    let mut graph = HashMap::<&str, HashSet<&str>>::new();
    for line in input.lines() {
        let (start, end) = line.split_once("-").unwrap();
        let mut insert = |a, b| match graph.get_mut(&a) {
            Some(h) => {
                h.insert(b);
            }
            None => {
                graph.insert(a, HashSet::from([b]));
            }
        };
        insert(start, end);
        insert(end, start);
    }
    graph
}

#[derive(Clone)]
struct Path<'a> {
    path: Vec<&'a str>,
    nodes: HashMap<&'a str, u32>,
}

impl<'a> Path<'a> {
    fn extend(&mut self, node: &'a str) {
        self.path.push(node);
        *self.nodes.entry(&node).or_insert(0) += 1;
    }
    fn last(&self) -> &'a str {
        self.path[self.path.len() - 1]
    }
    fn contains(&self, node: &str) -> bool {
        self.nodes.contains_key(node)
    }
}

fn is_upper(string: &str) -> bool {
    string.as_bytes()[0] <= b'Z'
}

fn part_1(input: &str) -> usize {
    let graph = build_graph(input);
    let mut to_develop = vec![Path {
        path: vec!["start"],
        nodes: HashMap::from([("start", 1)]),
    }];
    let mut done = Vec::<Path>::new();
    while to_develop.len() > 0 {
        let path = to_develop.pop().unwrap();
        let neighbours = &graph[path.last()];
        for neighbour in neighbours.iter() {
            if is_upper(neighbour) || !path.contains(neighbour) {
                let mut new_path = path.clone();
                new_path.extend(neighbour);
                if neighbour == &"end" {
                    done.push(new_path);
                } else {
                    to_develop.push(new_path);
                }
            }
        }
    }
    done.len()
}

fn admits_minor(path: &Path) -> bool {
    path.nodes
        .iter()
        .filter(|(k, _)| !is_upper(k))
        .map(|(_, v)| v)
        .max()
        .unwrap()
        < &2
}
fn part_2(input: &str) -> usize {
    let graph = build_graph(input);
    let mut to_develop = vec![Path {
        path: vec!["start"],
        nodes: HashMap::from([("start", 1)]),
    }];
    let mut done = Vec::<Path>::new();
    while to_develop.len() > 0 {
        let path = to_develop.pop().unwrap();
        let neighbours = &graph[path.last()];
        for neighbour in neighbours.iter() {
            if neighbour != &"start" {
                if is_upper(neighbour) || !path.contains(neighbour) || admits_minor(&path) {
                    let mut new_path = path.clone();
                    new_path.extend(neighbour);
                    if neighbour == &"end" {
                        done.push(new_path);
                    } else {
                        to_develop.push(new_path);
                    }
                }
            }
        }
    }
    done.len()
}

fn main() {
    let test_input = include_str!("../../../inputs/12_test.txt").trim();
    let real_input = include_str!("../../../inputs/12.txt").trim();
    assert_eq!(part_1(test_input), 10);
    println!("part 1: {}", part_1(real_input));

    assert_eq!(part_2(test_input), 36);
    let start = Instant::now();
    println!("part 2: {}, took {:?}", part_2(real_input), start.elapsed());
}
