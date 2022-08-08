package com.sheepcastle.chapter03;

public class Change {
	public static void main(String[] args) {
		int n = 1260;
		int cnt = 0;
		int count = 0;

		int[] coin_types = { 500, 100, 50, 10 };

		for (int i = 0; i < 4; i++) {
			int coin = coin_types[i];
			cnt += n / coin;

		}

	}
}
