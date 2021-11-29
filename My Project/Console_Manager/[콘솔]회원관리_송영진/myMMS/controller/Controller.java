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

    void run() throws Exception {
        MainUI.call();
        int toggle = Validate.inInt(sc, 0, 7);
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
                throw new ExitException();
        }
    }

    void register() throws Exception {
        String value[] = new String[6];
        ControlUI.registerInit();
        ControlUI.inputNewData("id");
        int id = Validate.isInt(sc);
        Validate.checkNewID(id, model);
        for (int i = 0; i < key.length; i++) {
            ControlUI.inputNewData(key[i]);
            value[i] = i == 5 ? Integer.toString(Validate.isInt(sc)) : sc.nextLine();
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

    void update() throws Exception {
        String newValue[] = new String[6];
        ControlUI.updateInit();
        ControlUI.inputData("id");
        int id = Validate.isInt(sc);
        Validate.checkExistID(id, model);
        String oldValue[] = model.getData(id);
        for (int i = 0; i < key.length; i++) {
            ControlUI.outputData(key[i], oldValue[i]);
            ControlUI.inputData(key[i]);
            newValue[i] = i == 5 ? Integer.toString(Validate.isInt(sc)) : sc.nextLine();
        }
        model.putData(id, key, newValue);
        ControlUI.updateSuccess();
    }

    void delete() throws Exception {
        ControlUI.deleteInit();
        ControlUI.inputData("id");
        int id = Validate.isInt(sc);
        Validate.checkExistID(id, model);
        model.removeData(id);
        ControlUI.deleteSuccess();
    }

    void search() throws Exception {
        ControlUI.searchInit();
        ControlUI.searchSelect();
        int toggle = Validate.inInt(sc, 1, 7) - 2;
        if (toggle == -1) {
            ControlUI.inputData("id");
            int id = Validate.isInt(sc);
            Validate.checkExistID(id, model);
            ControlUI.output(model.toString(id) + "\n");
            ControlUI.searchSuccess();
        } else {
            String data = "";
            boolean checkFound = false;
            ControlUI.inputData(key[toggle]);
            data = toggle == 5 ? Integer.toString(Validate.isInt(sc)) : sc.nextLine();
            for (int id : model.getAllID()) {
                if (model.getData(id)[toggle].equals(data)) {
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