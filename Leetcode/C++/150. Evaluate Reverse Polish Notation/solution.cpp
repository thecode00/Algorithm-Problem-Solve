// https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution
{
public:
    int evalRPN(vector<string> &tokens)
    {
        stack<int> st;

        for (string &token : tokens)
        {
            if (token == "+" || token == "-" || token == "*" || token == "/")
            {
                int b = st.top();
                st.pop();
                int a = st.top();
                st.pop();
                int result;

                if (token == "+")
                    result = a + b;
                else if (token == "-")
                    result = a - b;
                else if (token == "*")
                    result = a * b;
                else if (token == "/")
                    result = a / b; // 정수 나눗셈, trunc toward 0

                st.push(result);
            }
            else
            {
                st.push(stoi(token));
            }
        }

        return st.top();
    }
};
