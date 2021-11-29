package controller;

import java.util.Scanner;

import model.Model;
import view.ErrorUI;

class Validate {
    static boolean keepContinue(Scanner sc) {
        ErrorUI.keepContinue();
        if (sc.nextLine().equals("Y"))
            return true;
        return false;
    }

    static Integer isInteger(Scanner sc) {
        int cnt = 0;
        do {
            try {
                return Integer.parseInt(sc.nextLine());
            } catch (NumberFormatException e) {
                if (!Validate.keepContinue(sc))
                    break;
                if (cnt < 3)
                    ErrorUI.notIntError1();
                else
                    ErrorUI.notIntError2();
                cnt++;
            }
        } while (true);
        return null;
    }

    static Integer inInteger(Scanner sc, int n, int m) {
        int num, temp, cnt = 0;
        if (n > m) {
            temp = n;
            n = m;
            m = temp;
        }
        do {
            try {
                num = Integer.parseInt(sc.nextLine());
                if (n <= num && num <= m) {
                    return num;
                } else {
                    if (!Validate.keepContinue(sc))
                        break;
                    ErrorUI.intRangeError(n, m);
                }

            } catch (NumberFormatException e) {
                if (!Validate.keepContinue(sc))
                    break;
                if (cnt < 3)
                    ErrorUI.notIntError1();
                else
                    ErrorUI.notIntError2();
                cnt++;
            }

        } while (true);
        return null;
    }

    static boolean checkNewID(Integer id, Model model) {
        if (id == null)
            return false;
        if (model.isExistID(id)) {
            ErrorUI.idExistError(id);
            return false;
        }
        return true;
    }

    static boolean checkExistID(Integer id, Model model) {
        if (id == null)
            return false;
        if (model.isExistID(id))
            return true;
        ErrorUI.idNotFoundError(id);
        return false;
    }
}