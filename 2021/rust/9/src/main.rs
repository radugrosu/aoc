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

fn main() {
    let test_input = include_str!("../../../inputs/9_test.txt").trim();
    let real_input = include_str!("../../../inputs/9.txt").trim();
    assert_eq!(part_1(test_input), 15);
    println!("part 1: {}", part_1(real_input));
}
