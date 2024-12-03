use std::cmp;

pub fn longest_common_prefix(strs: Vec<String>) -> String {
    divideandconquer(&strs, 0, strs.len() - 1)
}

fn divideandconquer(strs: &Vec<String>, start: usize, end: usize) -> String {
    if start < end {
        let mid = start + (end - start) / 2;
        let left: String = divideandconquer(strs, start, mid);
        let right: String = divideandconquer(strs, mid + 1, end);

        let ans: String = find_prefix(left, right);
        return ans;
    }
    strs[start].to_string()
}

fn find_prefix(left: String, right: String) -> String {
    let mut prefix = String::new();

    for (lc, rc) in left.chars().zip(right.chars()) {
        if lc == rc {
            prefix.push(lc);
        } else {
            break;
        }
    }
    prefix
}
