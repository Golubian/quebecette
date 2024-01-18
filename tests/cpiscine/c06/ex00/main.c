/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gachalif <gachalif@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/01/18 13:59:51 by gachalif          #+#    #+#             */
/*   Updated: 2024/01/18 14:02:13 by gachalif         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

static void	ft_putstr(char *str)
{
	while (str[0] != 0)
		write(1, str++, 1);
}

int	main(int argC, char **argV)
{
	if (argC >= 1)
	{
		ft_putstr(argV[0]);
		write(1, "\n", 1);
	}
}
