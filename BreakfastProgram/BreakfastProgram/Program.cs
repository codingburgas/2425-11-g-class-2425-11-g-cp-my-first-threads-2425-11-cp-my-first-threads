﻿namespace BreakfastProgram;

class Program
{
    static void Main(string[] args)
    {
        for (int i = 0; i < 10; i++)
        {
            Console.Write("*");
            
            Thread.Sleep(1000); 
        }
    }
}