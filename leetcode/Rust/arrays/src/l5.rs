pub fn longest_palindrome(s: String) -> String {
    let sb = s.as_bytes();
    if s.len() == 1 {
        return s;
    }
    if s.len() == 2 {
        if sb[0] == sb[1] {
            return s;
        } else {
            return (sb[0] as char).to_string();
        }
    }

    let mut max_length = 0;
    let mut lp1 = 0;
    let mut lp2 = 0;

    for i in 0..s.len() {
        // Case 1: Odd length of palindrome (using one char as center)
        let mut p1 = i;
        let mut p2 = i;
        check_palindrome(sb, &mut p1, &mut p2, &mut max_length, &mut lp1, &mut lp2);
        // Case 2: Even length of palindrome (using two chars as center)
        if i + 1 < s.len() && sb[i] == sb[i + 1] {
            let mut p1 = i;
            let mut p2 = i + 1;
            check_palindrome(sb, &mut p1, &mut p2, &mut max_length, &mut lp1, &mut lp2);
        }
    }

    let result = &sb[lp1..lp2 + 1];
    String::from_utf8(result.to_vec()).unwrap()
}

fn check_palindrome(
    arr: &[u8],
    p1: &mut usize,
    p2: &mut usize,
    max_length: &mut usize,
    lp1: &mut usize,
    lp2: &mut usize,
) {
    // Expand while p1 and p2 is in range and chars coincide
    while *p1 <= *p2 && *p2 < arr.len() && arr[*p1] == arr[*p2] {
        if (*p2 - *p1 + 1) > *max_length {
            *max_length = *p2 - *p1 + 1;
            *lp1 = *p1;
            *lp2 = *p2;
        }
        // Expanding to left and right
        *p1 -= 1;
        *p2 += 1;
    }
}
