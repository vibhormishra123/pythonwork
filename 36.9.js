<script>


	// Store the maximum element
	var max = 0;

	// Store the index of
	// the maximum element
	var index = 0;

	// Traverse the array target
	for (i = 0; i < target.length; i++) {

		// If current element is
		// greater than max
		if (max < target[i]) {
			max = target[i];
			index = i;
		}
	}

	// If max element is 1
	if (max == 1)
		return true;

	// Traverse the array, target
	for (i = 0; i < target.length; i++) {

		// If current index is not equal to
		// maximum element index
		if (i != index) {

			// Update max
			max -= target[i];

			// If max is less than
			// or equal to 0,
			if (max <= 0)
				return false;
		}
	}

	// Update the maximum element
	target[index] = max;

	// Recursively call the function
	return isPossible(target);
}

// Driver Code
var target = [ 9, 3, 5 ];

res = isPossible(target);

if (res) {

	document.write("YES");
}
else {
	document.write("NO");
}
//
</script>
