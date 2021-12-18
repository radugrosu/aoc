use std::collections::HashSet;
const NEIGHBOURS: [(isize, isize); 8] = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
];

fn pop(set: &mut HashSet<(usize, usize)>) -> (usize, usize) {
    let elt = set.iter().next().cloned().unwrap();
    set.take(&elt).unwrap()
}

fn step(array: &mut Vec<Vec<u8>>) -> usize {
    let mut to_visit = HashSet::new();
    for i in 0..array.len() {
        for j in 0..array[0].len() {
            array[i][j] += 1;
            if array[i][j] > 9 {
                to_visit.insert((i, j));
            }
        }
    }
    let n = array.len();
    let m = array[0].len();
    if to_visit.len() > 0 {
        let mut flashed = HashSet::new();
        while to_visit.len() > 0 {
            let (x, y) = pop(&mut to_visit);
            flashed.insert((x, y));
            let neighbours = NEIGHBOURS
                .iter()
                .map(|&(dx, dy)| (x as isize + dx, y as isize + dy))
                .filter(|&(a, b)| 0 <= a && a < n as isize && 0 <= b && b < m as isize);
            for (a, b) in neighbours {
                let a = a as usize;
                let b = b as usize;
                (*array)[a][b] += 1;
                if !flashed.contains(&(a, b)) && array[a][b] > 9 {
                    to_visit.insert((a, b));
                }
            }
        }
        for &(a, b) in flashed.iter() {
            array[a][b] = 0;
        }
        flashed.len()
    } else {
        0
    }
}

fn part_1(input: &str, steps: usize) -> usize {
    let mut array = input
        .lines()
        .map(|l| {
            l.chars()
                .map(|i| i.to_digit(10).unwrap() as u8)
                .collect::<Vec<u8>>()
        })
        .collect::<Vec<_>>();
    (0..steps).fold(0, |a, _| a + step(&mut array))
}

fn part_2(input: &str, steps: usize) -> usize {
    let mut array = input
        .lines()
        .map(|l| {
            l.chars()
                .map(|i| i.to_digit(10).unwrap() as u8)
                .collect::<Vec<u8>>()
        })
        .collect::<Vec<_>>();
    let n = array.len() * array[0].len();
    for i in 1..=steps {
        if step(&mut array) == n {
            return i;
        }
    }
    return 0;
}
fn main() {
    let test_input = include_str!("../../../inputs/11_test.txt").trim();
    let real_input = include_str!("../../../inputs/11.txt").trim();
    assert_eq!(part_1(test_input, 100), 1656);
    println!("part 1: {}", part_1(real_input, 100));

    assert_eq!(part_2(test_input, 195), 195);
    println!("part 2: {}", part_2(real_input, 1000));
}
