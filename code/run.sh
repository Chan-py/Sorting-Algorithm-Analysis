#!/bin/bash

# 실행할 알고리즘들을 배열로 정의합니다.
ALGORITHMS=("library" "merge" "heap" "bubble" "insertion" "selection" "quick")

# 테스트할 리스트 파일 (필요에 따라 수정)
LIST_FILE="../dataset/test/testcase2.txt"

for alg in "${ALGORITHMS[@]}"; do
    echo "---------------------------------"
    echo "Running main.py with '$alg' algorithm"
    python main.py --algorithm "$alg" --list "$LIST_FILE"
    echo "---------------------------------"
done