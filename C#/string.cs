using System;
using System.IO;
using System.Linq;

namespace ConsoleApp1
{

    class Program
    {
      
      
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a series of number: (seperated by comma): ");
            var input = Console.ReadLine();
            var nums = input.Split(',');
            var maxNum = Convert.ToInt32(nums[0]);

            foreach (var str in nums)
            {
                var number = Convert.ToInt32(str);
                if(number > maxNum)
                {
                    maxNum = number;
                }

            }
            Console.WriteLine("Maximum number is " + maxNum);


        }
    }
}
