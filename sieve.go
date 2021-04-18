package main

import (
	"flag"
	"fmt"
	"math"
	"strconv"
)

func main() {

	flag.Parse()

	if len(flag.Args()) == 0 {

		fmt.Println("needs args")

	} else {

		targ, _ := strconv.ParseInt(flag.Args()[0], 0, 0)
		i := int64(3)

		for i < targ {
			if isPrime(i) {
				fmt.Printf("%v ", i)
			}
			i += 2
		}

	}

}

func isPrime(targ int64) bool {

	cv := float64(targ)
	cv = math.Sqrt(cv)
	cv = math.Ceil(cv)
	rg := int64(cv) + 1

	for i := int64(3); i < rg; i += 2 {
		if targ%i == 0 {
			return false
		}
	}

	return true
}
