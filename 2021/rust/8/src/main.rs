fn part_1(input: &str) -> usize {
    input
        .lines()
        .flat_map(|l| l.split_once("|").unwrap().1.split(" "))
        .filter(|p| matches!(p.len(), 2 | 3 | 4 | 7))
        .count()
}


fn main() {
    let test_input = include_str!("../../../inputs/8_test.txt").trim();
    let real_input = include_str!("../../../inputs/8.txt").trim();
    assert_eq!(part_1(test_input), 26);
    println!("part 1: {}", part_1(real_input));

    // assert_eq!(part_2(test_input), 168);
    // println!("part 2: {}", part_2(real_input));
}
