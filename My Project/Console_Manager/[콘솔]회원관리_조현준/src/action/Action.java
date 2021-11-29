package action;

import util.MemberDB;
import java.util.Scanner;

public interface Action {
    void execute(Scanner sc, MemberDB DB) throws Exception;
}