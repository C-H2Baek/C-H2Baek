package controller;

import java.util.Scanner;
import model.Model;
import view.ErrorUI;
import view.MainUI;

class NewIDException extends Exception {
    NewIDException(int id) {
        ErrorUI.idExistError(id);
    }
}

class ExistIDException extends Exception {
    ExistIDException(int id) {
        ErrorUI.idNotFoundError(id);
    }
}

class UserInterruptException extends Exception {
    UserInterruptException() {
        ErrorUI.userInterrupt();
    }
}

class ExitException extends Exception {
    ExitException() {
        MainUI.printExit();
    }
}

class Validate {
    static void keepContinue(Scanner sc) throws UserInterruptException {
        ErrorUI.keepContinue();
        if (!sc.nextLine().equals("Y"))
            throw new UserInterruptException();
    }

    static void validRun(Controller main) {
        do {
            try {
                main.run();
            } catch (ExitException eee) {
                break;
            } catch (UserInterruptException | NewIDException | ExistIDException ee) {

            } catch (Exception e) {
                e.printStackTrace();
            }
        } while (true);
    }

    static int isInt(Scanner sc) throws UserInterruptException {
        int cnt = 0;
        do {
            try {
                return Integer.parseInt(sc.nextLine());
            } catch (NumberFormatException e) {
                Validate.keepContinue(sc);
                if (cnt < 3)
                    ErrorUI.notIntError1();
                else
                    ErrorUI.notIntError2();
                cnt++;
            }
        } while (true);
    }

    static int inInt(Scanner sc, int n, int m) throws UserInterruptException {
        int num, temp;
        if (n > m) {
            temp = n;
            n = m;
            m = temp;
        }
        do {
            num = isInt(sc);
            if (n <= num && num <= m)
                return num;
            else {
                Validate.keepContinue(sc);
                ErrorUI.intRangeError(n, m);
            }
        } while (true);
    }

    static void checkNewID(int id, Model model) throws NewIDException {
        if (model.isExistID(id))
            throw new NewIDException(id);
    }

    static void checkExistID(int id, Model model) throws ExistIDException {
        if (!model.isExistID(id))
            throw new ExistIDException(id);
    }
}