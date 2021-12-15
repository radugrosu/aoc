fn part_1(input: &str) -> i32 {
    let pos = [(0, -1), (0, 1), (1, 0), (-1, 0)];
    let table = input
        .lines()
        .map(|l| {
            l.chars()
                .map(|c| c.to_digit(10).unwrap() as i32)
                .collect::<Vec<i32>>()
        })
        .collect::<Vec<Vec<i32>>>();

    let mut total = 0;
    for (y, line) in table.iter().enumerate() {
        for (x, h) in line.iter().enumerate() {
            let x = x as isize;
            let y = y as isize;
            if *h
                < pos
                    .iter()
                    .filter(|p| {
                        (y + p.1 >= 0)
                            && (y + p.1 < table.len() as isize)
                            && (x + p.0 >= 0)
                            && (x + p.0 < line.len() as isize)
                    })
                    .map(|p| ((x + p.0) as usize, (y + p.1) as usize))
                    .map(|p| table[p.1][p.0])
                    .min()
                    .unwrap()
            {
                total += 1 + h;
            }
        }
    }
    total
}
const NEXT: [(isize, isize); 4] = [(0, -1), (0, 1), (-1, 0), (1, 0)];

fn basin(map: &mut Vec<Vec<u8>>, x: usize, y: usize) -> usize {
    map[y][x] = b'9';
    NEXT.iter()
        .map(|(xx, yy)| ((x as isize + xx) as usize, (y as isize + yy) as usize))
        .fold(1, |acc, (x, y)| {
            match map.get(y).and_then(|l| l.get(x)).map(|&n| n < b'9') {
                Some(true) => acc + basin(map, x, y),
                _ => acc,
            }
        })
}
fn part_2() {
    let mut map = include_bytes!("../input.txt")
        .split(|&b| b == b'\n')
        .map(|l| l.to_vec())
        .collect::<Vec<_>>();

    let mut basins = vec![];
    for y in 0..map.len() {
        for x in 0..map[0].len() {
            (map[y][x] < b'9').then(|| basins.push(basin(&mut map, x, y)));
        }
    }

    basins.sort_unstable();
    println!("{}", basins.iter().rev().take(3).product::<usize>());
}


fn main() {
    let test_input = include_str!("../../../inputs/9_test.txt").trim();
    let real_input = include_str!("../../../inputs/9.txt").trim();
    assert_eq!(part_1(test_input), 15);
    println!("part 1: {}", part_1(real_input));

    assert_eq!(part_2(test_input), 168);
    println!("part 2: {}", part_2(real_input));
}
