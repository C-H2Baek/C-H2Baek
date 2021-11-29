package ui;

import java.util.Scanner;
import controller.MemberController;
import util.InputMismatchCheck;
import util.MemberDB;
import action.*;

public class MemberUi {
    public static void main(String[] args) {
        InputMismatchCheck menu = new InputMismatchCheck();
        MemberDB DB = new MemberDB();
        Scanner sc = new Scanner(System.in);
        MemberController memberController = new MemberController();
        boolean stop = true;
        while (stop) {
            Action action = null;
            System.out.println("========== 회원 데이터 관리 ==========");
            System.out.println("1.회원가입");
            System.out.println("2.회원 목록 보기");
            System.out.println("3.회원 정보 수정");
            System.out.println("4.회원 정보 삭제");
            System.out.println("5.회원 정보 검색");
            System.out.println("6.프로그램 종료");
            System.out.print("메뉴 번호 : ");
            switch (menu.Check("MENU")) {
                case 1:
                    action = new MemberRegistAction();
                    break;
                case 2:
                    action = new MemberListAction();
                    break;
                case 3:
                    action = new MemberUpdateAction();
                    break;
                case 4:
                    action = new MemberDeleteAction();
                    break;
                case 5:
                    action = new MemberSearchAction();
                    break;
                case 6:
                    System.out.println("프로그램 종료");
                    sc.close();
                    stop = false;
                    break;
                default:
                    System.out.println("1~6만 입력");
                    break;
            }
            if (action != null) {
                memberController.processRequest(sc, action, DB);
            }
        }
    }
}