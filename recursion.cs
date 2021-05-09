using System;
using System.IO;
using System.Linq;

namespace ConsoleApp1
{

    class Program
    {
        //using recursion
      public static int countfactorial(int num)
        {
          
        if(num == 1)
            {
                return num;
            }
        else
            {
                return num * countfactorial(num - 1);
            }
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a number: ");
            int num = Convert.ToInt32(Console.ReadLine());
            int total = countfactorial(num);
            Console.WriteLine("The factorial is " + total);
        }
    }
}
