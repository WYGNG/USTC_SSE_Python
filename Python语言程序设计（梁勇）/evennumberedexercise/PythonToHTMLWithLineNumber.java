/**
 * Usage: Copy this class to the folder, run it with java PythonToHTML * to generate
 *   HTM file for all the .py file in this folder. The generated .htm files are
 *   stored in the same folder
 */
import java.util.*;
import java.io.*;

public class PythonToHTMLWithLineNumber {
  static Scanner input;
  static Formatter output;
  static boolean stringToken = false;
  static String inputFileName;

  // Array of all Java keywords + true + false + null
  static String[] keywordString = {
      "and", "del", "from", "not", "while",  "nonlocal",
      "as",        "elif",      "global",    "or",        "with",     
      "assert",    "else",      "if",        "pass",      "yield",    
      "break",     "except",    "import",                  
      "class",        "from",      "in",        "raise",              
      "continue",  "finally",   "is",        "return",             
      "def",       "for",       "lambda",    "try",
      "True", "False", "None"};

  static Set keywordSet = new HashSet(Arrays.asList(keywordString));

  /** Main method */
  public static void main(String[] args) {
    try {
      for (int i = 0; i < args.length; i++) {
        if (args[i].endsWith(".py") &&
            ! (args[i].equals("PythonToHTML.py"))) {
          input = new Scanner(new File(args[i]));

          inputFileName = args[i];
          // -4 for .doc original files and -5 for .py original files
          String outputFileName = "c:\\idrive\\web\\py\\evennumberedexercisehtml\\" +
              args[i].substring(0, args[i].length() - 3) + "WithLineNumber.html";

          System.out.println("File " + args[i] + "'s HTML version is ");
          System.out.println(" stored to " + outputFileName);

          output = new Formatter(new File(outputFileName));

          JavaToHTML();
        }
      }
    }
    catch (Exception ex) {
    }
  }

  public static void JavaToHTML() {
    try {
      output.format("%s\r\n", "<html>");
      output.format("%s\r\n", "<head>");
      output.format("%s\r\n",
                    "<title>Introduction to Programming with Python 3 - " + inputFileName +
                    "</title>");
      output.format("%s\r\n",
                    "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1252\">");
      output.format("%s\r\n", "<style type = \"text/css\">");
      output.format("%s\r\n",
                    "body {font-family: \"Courier New\", sans-serif; font-size: 100%; color: black}");

      output.format("%s\r\n", ".keyword {color: #000080; font-weight: bold}");
 output.format("%s\r\n", ".comment {color: gray}");
 output.format("%s\r\n", ".literal {color: #0000ff}");

// Match the color in the text
// output.format("%s\r\n", ".keyword {color: black; font-weight: bold}");
//      output.format("%s\r\n", ".comment {color: #77797C}");
//      output.format("%s\r\n", ".literal {color: #007346; font-weight: bold}");
      output.format("%s\r\n", "</style>");

      output.format("%s\r\n", "</head>");
      output.format("%s\r\n", "<body>");
      
      output.format("%s\r\n", "<form action = \"" + 
          inputFileName.substring(0, inputFileName.length() - 3) + ".html" + "\" method = \"get\">");
      output.format("%s\r\n", "<input type = \"submit\" value = \"Show Code Without Line Numbers\" />");
      output.format("%s\r\n", "</form>");
      
      output.format("%s\r\n", "<pre>");

      String pySourceText = "";
      String temp;

      // Read all lines
      int lineNumber = 1;
      while (input.hasNext()) {
        temp = input.nextLine();
        pySourceText += String.format("%2d", lineNumber++) + "&nbsp;&nbsp;" + temp + "\r\n";
      }

      pySourceText = pySourceText.replaceAll(">", "&gt;");
      pySourceText = pySourceText.replaceAll("<", "&lt;");
      translateToHTML(pySourceText);

      output.format("%s\r\n", "</pre>");
      output.format("%s\r\n", "</body>");
      output.format("%s\r\n", "</html>");
    }
    catch (Exception ex) {
      System.out.println(ex);
    }
    finally {
      try {
        input.close();
        output.close();
      }
      catch (Exception ex) {
      }
    }
  }

  /** Translate Python source code to HTML */
  static void translateToHTML(String text) throws Exception {
    text = text.replaceAll("# ", "LINECOMMENT");
    text = text.replaceAll("/\\*", "BLOCKCOMMENT");

    String token;

    while (text != null && text.length() > 0) {
      // * and / are in conflict with /* and //
       String[] parts = text.split("[%\\+\\-\\*/\r\n\t \\[\\].;(){},:]", 2);

      token = parts[0];

      if (token.length() > 1 && token.startsWith("LINECOMMENT")) {
        output.format("%s", "<span class = \"comment\">");
        parts = text.split("\r\n", 2);
        text = parts[1];
        output.format("%s", parts[0].replaceAll("LINECOMMENT", "# "));
        output.format("%s", "</span>\r\n");
        continue;
      }
      else if (token.length() > 1 && token.startsWith("BLOCKCOMMENT")) {
        output.format("%s", "<span class = \"comment\">");
        parts = text.split("\\*/", 2);
        text = parts[1];

        output.format("%s", parts[0].replaceAll("BLOCKCOMMENT", "/*") + "*/");
        output.format("%s", "</span>");
        continue;
      }
      else if (token.length() > 1 && token.matches("'\\w'*")) {
        output.format("%s", "<span class = \"literal\">");
        output.format("%s", token);
        output.format("%s", "</span>");
      }

      else if (token.startsWith("\"") && token.endsWith("\"") &&
               (token.length() > 1)) {
        output.format("%s", "<span class = \"literal\">" + token
                      + "</span>");
      }
      else if (token.startsWith("'") && token.endsWith("'") &&
               (token.length() > 1)) {
        output.format("%s", "<span class = \"literal\">" + token
                      + "</span>");
      }
      else if (token.equals("' '")) {
        output.format("%s", "<span class = \"literal\">" + token
                      + "</span>");
      } 
      else if (token.startsWith("\"") && token.endsWith("\"") &&
               (token.length() == 1)) {
        if (stringToken) {
          output.format("%s", token + "</span>");
          stringToken = false;
        }
        else {
          output.format("%s", "<span class = \"literal\">" + token);
          stringToken = true;
        }
      }
      else if (token.startsWith("\"")) {
        output.format("%s", "<span class = \"literal\">" + token);
        stringToken = true;
      }
      else if (token.endsWith("\"") && (!token.endsWith("\\\""))) {
        output.format("%s", token);
        output.format("%s", "</span>");
        stringToken = false;
      }
      else if (token.matches("\\d+")) { // Check if numeric
        output.format("%s", "<span class = \"literal\">" + token +
                      "</span>");
      }
      else if (!stringToken && keywordSet.contains(token)) {
        output.format("%s", "<span class = \"keyword\">" + token +
                      "</span>");
      }
      else {
        output.format("%s", token);
      }

      if (token.length() < text.length()) {
        if (text.charAt(token.length()) == '<')
           output.format("%s", "&lt;");
        else if (text.charAt(token.length()) == '>')
          output.format("%s", "&gt;");
        else
          output.format("%s", text.charAt(token.length()));
      }

      if (parts.length == 2) {
        text = parts[1];
      }
    }
  }
}
