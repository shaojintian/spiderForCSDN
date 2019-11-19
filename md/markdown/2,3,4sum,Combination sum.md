3，4sum用双指针

CombinationSum 用递归

```java
package algorithms_4th;


import java.awt.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

/**
 * 
 * 3sum,4sum,combination sum
 * 双指针法：先排序，sum<target:p1++;sum>target:p2--;移动范围减小-->为了p1,p2碰头
 *
 */
public class ksum {

	static int[] arr = { 1,  5, 7, 2, 6, 9, 4 ,3};
	
	static int[] res = new int[2];

	public static int[] sum2(int target) {
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
		int index1, index2;
		for (int i = 0; i < arr.length; i++) {
			if (map.containsKey(target - arr[i])) {
				index1 = map.get(target - arr[i]) + 1;
				index2 = i + 1;
				res[0] = Math.min(index1, index2);
				res[1] = Math.max(index1, index2);
			}
			// initialize map
			map.put(arr[i], i);
		}
		return res;
	}

	public static ArrayList<ArrayList<Integer>> sum3(int target) {
		ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> list = null;
		int p1, p2, sum;

		Arrays.sort(arr);
		for (int i = 0; i < arr.length - 1; i++) {
			p1 = i + 1;
			p2 = arr.length - 1;
			if (i == 0 || arr[i] > arr[i - 1]) {

				while (p2 > p1) {
					sum = arr[i] + arr[p1] + arr[p2];

					if (sum == target) {
						list = new ArrayList<Integer>();
						list.add(arr[i]);
						list.add(arr[p1]);
						list.add(arr[p2]);
						
						res.add(list);
						p1++;
						p2--;
						while (p1 < p2 && arr[p1] == arr[p1 - 1])
							p1++;
						while (p1 < p2 && arr[p2] == arr[p2 + 1])
							p2--;
					} else if(sum>target){
						p2--;
					}else {
						p1++;
					}

				}
			}
		}

		return res;
	}
	
	public static ArrayList<ArrayList<Integer>> sum4(int target) {
		ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> list = null;
		int p1, p2, sum;

		Arrays.sort(arr);
		for (int i = 0; i < arr.length - 1; i++) {
			for (int j = i+1; j < arr.length; j++) {
				p1 = j + 1;
				p2 = arr.length - 1;
				if (j == 0 || arr[j] > arr[j - 1]) {

					while (p2 > p1) {
						sum = arr[i] +arr[j]+ arr[p1] + arr[p2];

						if (sum == target) {
							list = new ArrayList<Integer>();
							list.add(arr[i]);
							list.add(arr[j]);
							list.add(arr[p1]);
							list.add(arr[p2]);
							
							res.add(list);
							p1++;
							p2--;
							while (p1 < p2 && arr[p1] == arr[p1 - 1])
								p1++;
							while (p1 < p2 && arr[p2] == arr[p2 + 1])
								p2--;
						} else if(sum>target){
							p2--;
						}else {
							p1++;
						}

					}
				}
				
			}
			
		}

		return res;
	}
	
	public static ArrayList<ArrayList<Integer>> combinationSum(int target) {
		ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> list = new ArrayList<>();
		int[] candidates=arr;
		Arrays.sort(candidates);
		recursive_sum(0,list,target,res,candidates);
		
		return res;
	}
	public static void recursive_sum(int i,ArrayList<Integer> sub_list,int target,
									ArrayList<ArrayList<Integer>> res, int[]candidates) {
		if(target==0) {
			res.add(new ArrayList<>(sub_list));
			return ;
		}
		for (int j = i; j < candidates.length; j++) {               
			if (candidates[j]<=target) {
				sub_list.add(candidates[j]);
				
				
				recursive_sum(j, sub_list, target-candidates[j], res,candidates );            
				sub_list.remove(sub_list.size()-1);
				
			}
		}
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// int[] res=sum2(10);
		ArrayList<ArrayList<Integer>> res3 = sum3(7);
		ArrayList<ArrayList<Integer>> res4 = sum4(10);
		ArrayList<ArrayList<Integer>> combination_sum=combinationSum(4);
		
		System.out.println("sum3:");
		for (int i = 0; i < res3.size(); i++) {
			for (int j = 0; j < 3; j++) {
				System.out.print(res3.get(i).get(j) + " ");
			}
			System.out.println();
		}
		System.out.println("sum4:");
		for (int i = 0; i < res4.size(); i++) {
			for (int j = 0; j < 4; j++) {
				System.out.print(res4.get(i).get(j) + " ");
			}
			System.out.println();
		}
		
		System.out.println("Combination_sum:");
		for (int i = 0; i < combination_sum.size(); i++) {
			for (int j = 0; j < combination_sum.get(i).size(); j++) {
				System.out.print(combination_sum.get(i).get(j) + " ");
			}
			System.out.println();
		}

	}

}


```

