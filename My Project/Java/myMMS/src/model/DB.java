package model;

import java.util.LinkedHashMap;
import java.util.Set;
import java.util.TreeMap;

class DB {
    private class PersonalData extends LinkedHashMap<String, String> {
    }

    private TreeMap<Integer, PersonalData> data = new TreeMap<Integer, PersonalData>();

    void put(int id) {
        PersonalData info = new PersonalData();
        data.put(id, info);
    }

    void put(int id, String key, String value) {
        data.get(id).put(key, value);
    }

    PersonalData get(int id) {
        return data.get(id);
    }

    String get(int id, String key) {
        return data.get(id).get(key);
    }

    Set<Integer> getKeySet() {
        return data.keySet();
    }

    Set<String> getKeySet(int id) {
        return data.get(id).keySet();
    }

    void remove(int id) {
        data.remove(id);
    }
}