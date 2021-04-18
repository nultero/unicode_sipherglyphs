#![allow(dead_code)]
use std::env;

fn main() {

    let mut start = 3;

    let mut targ: i64 = 0;
    // let mut primes: Vec<i64> = vec![2];

    let args: Vec<String> = env::args().collect();
    if args.len() > 1 && args.len() < 3 {
        for rg in 1..args.len() {
            targ = args[rg].parse().unwrap();
        }
        print!("2 ");
        let trg = targ as i64;
        while start < trg {
            if is_prime(start) {
                // primes.push(start);
                print!("{} ", start)
            } start += 2;
        }

    } else if args.len() == 1 || args.len() > 2 {
        println!("sieve just wants a number, man");
    }
}



fn is_prime(rg: i64) -> bool {

    let target = ((rg as f64).sqrt().ceil() as i64) + 1;

    let mut i = 3;
    while i < target {
        if rg % i == 0 {
            return false;
        } i += 2;
    }
    return true;
}
