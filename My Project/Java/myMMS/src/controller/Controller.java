package controller;

import java.util.Scanner;

import model.Model;
import model.TestModel;
import view.ControlUI;
import view.MainUI;

class Controller {
    Model model;
    Scanner sc;
    final String key[] = { "name", "email", "address", "hobby", "tel", "age" };

    void run() {
        boolean stop = false;
        Integer toggle;
        do {
            MainUI.call();
            toggle = Validate.inInteger(sc, 0, 7);
            if (toggle == null)
                continue;
            switch (toggle) {
            case 0: // test mode
                testMode();
                break;
            case 1:
                register();
                break;
            case 2:
                show();
                break;
            case 3:
                update();
                break;
            case 4:
                delete();
                break;
            case 5:
                search();
                break;
            case 6:
                initialize();
                break;
            case 7:
                stop = true;
                MainUI.printExit();
                break;
            }
        } while (!stop);
    }

    void register() {
        String value[] = new String[6];
        ControlUI.registerInit();
        ControlUI.inputNewData("id");
        Integer id = Validate.isInteger(sc);
        if (!Validate.checkNewID(id, model)) {
            ControlUI.registerFail();
            return;
        }
        for (

                int i = 0; i < key.length; i++) {
            ControlUI.inputNewData(key[i]);
            if (i == 5) {
                Integer age = Validate.isInteger(sc);
                if (age == null) {
                    ControlUI.registerFail();
                    return;
                }
                value[i] = Integer.toString(age);
            } else
                value[i] = sc.nextLine();
        }
        model.makeID(id);
        model.putData(id, key, value);
        ControlUI.registerSuccess();
    }

    void show() {
        ControlUI.showInit();
        String result[] = model.getAllData();
        for (String text : result)
            ControlUI.output(text + "\n");
    }

    void update() {
        String newValue[] = new String[6];
        ControlUI.updateInit();
        ControlUI.inputData("id");
        Integer id = Validate.isInteger(sc);
        if (!Validate.checkExistID(id, model)) {
            ControlUI.updateFail();
            return;
        }
        String oldValue[] = model.getData(id);
        for (int i = 0; i < key.length; i++) {
            ControlUI.outputData(key[i], oldValue[i]);
            ControlUI.inputData(key[i]);
            if (i == 5) {
                Integer age = Validate.isInteger(sc);
                if (age == null) {
                    ControlUI.updateFail();
                    return;
                }
                newValue[i] = Integer.toString(age);
            } else
                newValue[i] = sc.nextLine();
        }
        model.putData(id, key, newValue);
        ControlUI.updateSuccess();
    }

    void delete() {
        ControlUI.deleteInit();
        ControlUI.inputData("id");
        Integer id = Validate.isInteger(sc);
        if (!Validate.checkExistID(id, model)) {
            ControlUI.deleteFail();
            return;
        }
        model.removeData(id);
        ControlUI.deleteSuccess();
    }

    void search() {
        ControlUI.searchInit();
        ControlUI.searchSelect();
        Integer toggle = Validate.inInteger(sc, 1, 7);
        if (toggle == null) {
            ControlUI.searchFail();
            return;
        }
        if (toggle == 1) {
            ControlUI.inputData("id");
            Integer id = Validate.isInteger(sc);
            if (!Validate.checkExistID(id, model)) {
                ControlUI.searchFail();
                return;
            }
            ControlUI.output(model.toString(id) + "\n");
            ControlUI.searchSuccess();
        } else {
            String data = "";
            boolean checkFound = false;
            ControlUI.inputData(key[toggle - 2]);
            if (toggle == 7) {
                Integer age = Validate.isInteger(sc);
                if (age == null) {
                    ControlUI.searchFail();
                    return;
                }
                data = Integer.toString(age);
            } else {
                data = sc.nextLine();
            }
            for (int id : model.getAllID()) {
                if (model.getData(id)[toggle - 2].equals(data)) {
                    checkFound = true;
                    ControlUI.output(model.toString(id) + "\n");
                }
            }
            if (checkFound)
                ControlUI.searchSuccess();
            else
                ControlUI.searchNotFound();
        }

    }

    void initialize() {
        model = new Model();
        sc = new Scanner(System.in);
    }

    void testMode() {
        model = new TestModel(100);
    }
}