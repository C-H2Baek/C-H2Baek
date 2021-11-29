package model;

public class Model {
    protected DB dataBase = new DB();

    public Boolean isExistID(int id) {
        if (dataBase.get(id) == null)
            return false;
        return true;
    }

    public String toString(int id) {
        String result = id + "-->";
        for (String key : dataBase.getKeySet(id))
            result += String.format("[%s: %s]", key, dataBase.get(id, key));
        return result;
    }

    public void makeID(int id) {
        dataBase.put(id);
    }

    public String[] getData(int id) {
        String result[] = new String[dataBase.getKeySet(id).size()];
        int cnt = 0;
        for (String key : dataBase.getKeySet(id))
            result[cnt++] = dataBase.get(id, key);
        return result;
    }

    public void putData(int id, String key[], String value[]) {
        for (int i = 0; i < key.length; i++)
            dataBase.put(id, key[i], value[i]);
    }

    public String[] getAllData() {
        String result[] = new String[dataBase.getKeySet().size()];
        int cnt = 0;
        for (int id : dataBase.getKeySet())
            result[cnt++] = toString(id);
        return result;
    }

    public int[] getAllID() {
        int cnt = 0, result[] = new int[dataBase.getKeySet().size()];
        for (int i : dataBase.getKeySet())
            result[cnt++] = i;
        return result;
    }

    public void removeData(int id) {
        dataBase.remove(id);
    }
}