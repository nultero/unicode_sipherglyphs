use std::env;
// use std::num;


fn main() {

    let x: &str;
    let start = 3.0f64;
    let mut targ: i32 = 0;

    let args: Vec<String> = env::args().collect();
    if args.len() > 1 && args.len() < 3 {
        for rg in 1..args.len() {
            // println!("{:?}", args[rg]);
            targ = args[rg].parse().unwrap();
        }
    }
    
    // const CHARS: &str = "ⴱⴲⴳⴴⴵⴶⴷⴸⴹⴺⴼⴽⴾⴿⵀⵁⵃⵄⵅⵆⵇⵈⵉⵊⵋⵌⵍⵎⵐⵒⵓⵖⵗⵘⵙⵚⵛⵜⵝⵞⵟⵠⵡⵢⵣⵤⵥⵦ";
    
    // let mut i = 0;
    // for char in CHARS.chars() {
    //     i += 1;
    //     println!("{} == {}", char, i);

    // }
    // println!("{}", CHARS.len());
    println!("targ's been pushed out to {}", (targ*2));
    


}