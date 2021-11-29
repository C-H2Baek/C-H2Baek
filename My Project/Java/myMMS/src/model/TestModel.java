package model;

public class TestModel extends Model {
    public TestModel(int n) {
        for (int i = 0; i < n; i++) {
            String[] value = new String[6];
            dataBase.put(i);
            value[0] = randChar(3);
            value[1] = randChar(5 + (int) (Math.random() * 5)) + "@" + randChar(5) + ".com";
            value[2] = randChar(3 + (int) (Math.random() * 7)) + "/" + randChar(3 + (int) (Math.random() * 7)) + "/"
                    + randChar(3 + (int) (Math.random() * 7));
            value[3] = randChar(3 + (int) (Math.random() * 7));
            value[4] = randInt(3) + "-" + randInt(4) + "-" + randInt(4);
            value[5] = Integer.toString(1 + (int) (Math.random() * 9)) + randInt(1);
            for (int j = 0; j < 6; j++) {
                dataBase.put(i, key[j], value[j]);
            }
        }
    }

    final String key[] = { "name", "email", "address", "hobby", "tel", "age" };

    String randInt(int n) {
        String result = "";
        for (int i = 0; i < n; i++)
            result += Integer.toString((int) (Math.random() * 10));
        return result;
    }

    String randChar(int n) {
        String result = "";
        for (int i = 0; i < n; i++)
            result += Character.toString((char) ('a' + (int) (Math.random() * 26)));
        return result;
    }
}
