class Node {
    public static Node[] kids;
    public static int[][] data;

    public Node(int[][] data) {
        Node.data = data;
        Node.kids = new Node[getNumOfKids()];
        createKids();
    }

    public static void setData(int[][] arr) {
        Node.data = arr;
    }

    public static int findZero(int[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                if (arr[i][j] == 0) {
                    return i * 10 + j;
                }
            }
        }
        return -1;
    }

    public static int above(int location) {
        if (location >= 10) {
            return location - 10;
        } else {
            return -1;
        }
    }

    public static int bellow(int location) {
        if (location < 20) {
            return location + 10;
        } else {
            return -1;
        }
    }

    public static int right(int location) {
        if (location % 10 > 0) {
            return location - 1;
        } else {
            return -1;
        }
    }

    public static int left(int location) {
        if (location % 10 < 2) {
            return location + 1;
        } else {
            return -1;
        }
    }

    public static int[][] exchange(int location1, int location2) {
        // Create a copy of the current data
        int[][] data2 = new int[data.length][data[0].length];
        for (int i = 0; i < data.length; i++) {
            System.arraycopy(data[i], 0, data2[i], 0, data[i].length);
        }

        int row1 = location1 / 10;
        int col1 = location1 % 10;
        int row2 = location2 / 10;
        int col2 = location2 % 10;

        if (row1 >= 0 && row1 < data2.length && col1 >= 0 && col1 < data2[0].length &&
                row2 >= 0 && row2 < data2.length && col2 >= 0 && col2 < data2[0].length) {
            int temp = data2[row1][col1];
            data2[row1][col1] = data2[row2][col2];
            data2[row2][col2] = temp;
        }

        return data2;
    }


    public static int[][] getData() {
        return data;
    }

    public static Node[] getKids() {
        return kids;
    }

    public static void setKids(Node[] kids) {
        Node.kids = kids;
    }

    public static int firstFreeLocation(Node[] lst) {
        for (int i = 0; i < lst.length; i++) {
            if (lst[i] != null) {
                return i;
            }
        }
        return -1;
    }

    public static void createKids() {
        if (left(findZero(Node.data)) != -1) {
            kids[firstFreeLocation(kids)] = new Node(exchange(findZero(Node.data), left(findZero(Node.data))));
        }
        if (right(findZero(Node.data)) != -1) {
            kids[firstFreeLocation(kids)] = new Node(exchange(findZero(Node.data), right(findZero(Node.data))));
        }
        if (above(findZero(Node.data)) != -1) {
            kids[firstFreeLocation(kids)] = new Node(exchange(findZero(Node.data), above(findZero(Node.data))));
        }
        if (bellow(findZero(Node.data)) != -1) {
            kids[firstFreeLocation(kids)] = new Node(exchange(findZero(Node.data), bellow(findZero(Node.data))));
        }
    }

    public static int getNumOfKids() {
        int numOfKids = 0;
        if (left(findZero(Node.data)) != -1) {
            numOfKids++;
        }
        if (right(findZero(Node.data)) != -1) {
            numOfKids++;
        }
        if (above(findZero(Node.data)) != -1) {
            numOfKids++;
        }
        if (bellow(findZero(Node.data)) != -1) {
            numOfKids++;
        }
        return numOfKids;
    }

}
